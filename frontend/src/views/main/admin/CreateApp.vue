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
import { IApp, IAppCreate } from "@/interfaces";
import { readAdminApps } from "@/store/admin/getters";
import { dispatchGetApps, dispatchCreateApp } from "@/store/admin/actions";

@Component
export default class CreateApp extends Vue {
  public valid = false;
  public name: string = "";
  public description: string = "";
  public app: IApp = {} as any;

  public async mounted() {
    this.reset();
  }

  public reset() {
    this.name = "";
    this.description = "";
    this.app = {} as any;
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
