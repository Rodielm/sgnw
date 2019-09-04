<template>
  <v-container fluid>
    <v-card class="ma-3 pa-3">
      <v-card-title primary-title>
        <div class="headline primary--text">Edit App</div>
      </v-card-title>
      <v-card-text>
        <template>
          <v-form v-model="valid" ref="form" lazy-validation>
            <v-text-field label="Name" v-model="name" required></v-text-field>
            <v-text-field label="Description" v-model="description" required></v-text-field>
            <v-text-field label="Version" v-model="version"></v-text-field>
            <v-btn color="primary" dark @click.stop="dialog = true">Add Language</v-btn>
            <v-dialog v-model="dialog" max-width="360">
              <v-card>
                <v-card-title>
                  <span class="headline">Add Language</span>
                </v-card-title>
                <v-card-text>
                  <UploadLangFile></UploadLangFile>
                </v-card-text>
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn color="blue darken-1" flat="flat" @click="dialogClose">Close</v-btn>
                  <v-btn color="blue darken-1" flat="flat" @click="dialogOk">Ok</v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>
            <v-chip
              v-for="f in fileUploads"
              :key="f.filename"
              @input="onClose(f)"
              close
            >{{f.filename}}</v-chip>
          </v-form>
        </template>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn @click="cancel">Cancel</v-btn>
        <v-btn @click="reset">Reset</v-btn>
        <v-btn @click="submit" :disabled="!valid">Save</v-btn>
      </v-card-actions>
    </v-card>
  </v-container>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import UploadLangFile from '@/components/UploadLangFile.vue';
import { IApp, IAppUpdate, IAppLang, IFileUpload } from '@/interfaces';
import {
  dispatchUpdateApp,
  dispatchRemoveFileLocal,
  dispatchCreateUser,
  dispatchAddFileLocal,
  dispatchRemoveAppLangs,
} from '@/store/admin/actions';
import {
  readAdminOneApp,
  readAdminApps,
  readAdminFiles,
} from '@/store/admin/getters';
import { commitRemoveAllFile, commitAddFile } from '../../../store/admin/mutations';

@Component({
  components: {
    UploadLangFile,
  },
})
export default class EditApp extends Vue {
  public valid = true;
  public dialog = false;
  public name: string = '';
  public description: string = '';
  public version: string = '';
  public fileUploads: IFileUpload[] = [];
  public deletedFileUploads: IFileUpload[] = [];

  public async mounted() {
    this.reset();
  }

  public reset() {
    this.name = '';
    this.description = '';
    this.version = '';
    this.$validator.reset();
    if (this.app) {
      this.name = this.app.name;
      this.description = this.app.description;
      this.version = this.app.version;
      if (this.app.app_langs) {
        this.app.app_langs.forEach((f) => {
          const appLang: IFileUpload = {
            version: f.version,
            lang: f.lang,
            filename: f.filename,
          };
          this.fileUploads.push(appLang);
        });
        if (this.fileUploads) {
          commitRemoveAllFile(this.$store);
          this.fileUploads.forEach((file) => {
            commitAddFile(this.$store, file);
          });
        }
      }
    }
  }

  public cancel() {
    this.$router.back();
  }

  public async onClose(file) {
    // deleted file local component
    this.fileUploads = this.fileUploads.filter((f) => f !== file);

    // check if exist this file on deleted list
    if (this.deletedFileUploads.some((f) => f.lang!.id === file.lang.id)) {
      // remove file on deleted list if exist
      this.deletedFileUploads = this.deletedFileUploads.filter(
        (f) => f.lang!.id !== file.lang.id,
      );
    } else {
      // add file to deleted list if doesn't exist
      this.deletedFileUploads.push(file);
    }
    // remove file on state management
    await dispatchRemoveFileLocal(this.$store, file);
  }

  public dialogClose() {
    this.dialog = false;
  }
  public dialogOk() {
    this.dialog = false;
    this.fileUploads = readAdminFiles(this.$store);
  }

  public async submit() {
    if (await this.$validator.validateAll()) {
      const updatedApp: IAppUpdate = {
        app_langs: [],
      };
      if (this.name) {
        updatedApp.name = this.name;
      }
      if (this.description) {
        updatedApp.description = this.description;
      }
      if (this.version) {
        updatedApp.version = this.version;
      }

      if (this.fileUploads) {
        this.fileUploads.forEach((f) => {
          // const filename = f.lang!.name + "_" + Date.now() + "_" + f.filename;
          const appLang: IAppLang = {
            version: f.version,
            filename: f.filename,
            lang: f.lang,
          };
          updatedApp.app_langs.push(appLang);
        });

        this.deletedFileUploads.forEach((f) => {
          dispatchRemoveAppLangs(this.$store, {
            idApp: this.app!.id,
            idLang: f.lang!.id,
            file: f,
          });
        });
      }

      await dispatchUpdateApp(this.$store, {
        id: this.app!.id,
        app: updatedApp,
      });
      this.$router.push('/main/admin/apps');
    }
  }

  get app() {
    return readAdminOneApp(this.$store)(+this.$router.currentRoute.params.id);
  }
}
</script>
