<template>
  <v-container fluid>
    <v-card class="ma-3 pa-3">
      <v-card-title primary-title>
        <div class="headline primary--text">Create App</div>
      </v-card-title>
      <v-card-text>
        <template>
          <v-form v-model="valid" ref="form" lazy-validation>
            <v-text-field label="Name" v-model="name" required></v-text-field>
            <v-text-field label="Description" v-model="description"></v-text-field>
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
import { IApp, IAppCreate, ILang, IAppLang, IFileUpload } from '@/interfaces';
import {
  readAdminApps,
  readAdminLangs,
  readAdminFiles,
} from '@/store/admin/getters';
import {
  dispatchGetApps,
  dispatchCreateApp,
  dispatchGetLangs,
  dispatchRemoveFileLocal,
} from '@/store/admin/actions';

@Component({
  components: {
    UploadLangFile,
  },
})
export default class CreateApp extends Vue {
  public valid = false;
  public dialog = false;
  public name: string = '';
  public description: string = '';
  public version: string = '';
  public app: IApp = {} as any;
  public fileUploads: IFileUpload[] = [];

  public async mounted() {
    await dispatchGetLangs(this.$store);
    this.reset();
  }

  public async onClose(file) {
    this.fileUploads = this.fileUploads.filter((f) => f !== file);
    await dispatchRemoveFileLocal(this.$store, file);
  }

  public reset() {
    this.name = '';
    this.description = '';
    this.app = {} as any;
    this.fileUploads = [];
    this.$validator.reset();
  }

  public dialogClose() {
    this.dialog = false;
  }

  public dialogOk() {
    this.dialog = false;
    this.fileUploads = readAdminFiles(this.$store);
  }

  public cancel() {
    this.$router.back();
  }

  public async submit() {
    if (await this.$validator.validateAll()) {
      const updatedApp: IAppCreate = {
        name: this.name,
        app_langs: [],
      };
      if (this.description) {
        updatedApp.description = this.description;
      }
      if (this.name) {
        updatedApp.name = this.name;
      }
      if (this.description) {
        updatedApp.description = this.description;
      }

      if (this.fileUploads) {
        this.fileUploads.forEach((f) => {
          const filename = f.file!.name + '_' + f.lang!.name + '_' + Date.now();
          const appLang: IAppLang = {
            version: f.version,
            filename,
            lang: f.lang,
          };
          updatedApp.app_langs.push(appLang);
        });
      }

      await dispatchCreateApp(this.$store, updatedApp);
      this.$router.push('/main/admin/apps');
    }
  }
}
</script>
