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
            <v-btn color="primary" dark @click.stop="dialog = true">Add Language</v-btn>
            <v-dialog v-model="dialog" max-width="360">
              <v-card>
                <v-card-title>
                  <span class="headline">Add Language</span>
                </v-card-title>
                <v-card-text>
                  <v-container>
                    <v-layout wrap>
                      <v-flex>
                        <v-select
                          :items="langs"
                          name="lang"
                          label="Select a language"
                          v-model="lang"
                          item-text="name"
                          return-object
                          required
                        ></v-select>
                      </v-flex>
                      <v-flex>
                        <UploadButton></UploadButton>
                      </v-flex>
                    </v-layout>
                  </v-container>
                  <small>*indicates required field</small>
                </v-card-text>
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn color="blue darken-1" flat="flat" @click="dialog = false">Close</v-btn>
                  <v-btn color="blue darken-1" flat="flat" @click="dialog = false">Ok</v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>
            <UploadButton></UploadButton>
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
import { Component, Vue } from "vue-property-decorator";
import UploadButton from "@/components/UploadButton.vue";
import { IApp, IAppCreate, ILang } from "@/interfaces";
import { readAdminApps, readAdminLangs } from "@/store/admin/getters";
import {
  dispatchGetApps,
  dispatchCreateApp,
  dispatchGetLangs
} from "@/store/admin/actions";

@Component({
  components: {
    UploadButton
  }
})
export default class CreateApp extends Vue {
  public valid = false;
  public dialog = false;
  public name: string = "";
  public description: string = "";
  public app: IApp = {} as any;
  public lang: ILang = {} as any;

  public async mounted() {
    await dispatchGetLangs(this.$store);
    this.reset();
  }

  get langs() {
    return readAdminLangs(this.$store);
  }

  public reset() {
    this.name = "";
    this.description = "";
    this.app = {} as any;
    this.lang = {} as any;
    this.$validator.reset();
  }

  public cancel() {
    this.$router.back();
  }

  public async submit() {
    if (await this.$validator.validateAll()) {
      const updatedApp: IAppCreate = {
        name: this.name
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
      await dispatchCreateApp(this.$store, updatedApp);
      this.$router.push("/main/admin/apps");
    }
  }
}
</script>
