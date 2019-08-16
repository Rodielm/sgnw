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
import { IApp, IAppUpdate } from "@/interfaces";
import { dispatchUpdateApp } from "@/store/admin/actions";
import { readAdminOneApp, readAdminApps } from "@/store/admin/getters";

@Component
export default class EditApp extends Vue {
  public valid = true;
  public name: string = "";
  public description: string = "";

  public async mounted() {
    this.reset();
  }

  public reset() {
    this.name = "";
    this.description = "";
    this.$validator.reset();
    if(this.app){
      this.name = this.app.name;
      this.description = this.app.description;
    }
  }

  public cancel() {
    this.$router.back();
  }

  public async submit() {
    if (await this.$validator.validateAll()) {
      const updatedApp: IAppUpdate = {};
      if (this.name) {
        updatedApp.name = this.name;
      }
      if (this.description) {
        updatedApp.description = this.description;
      }

      await dispatchUpdateApp(this.$store, {
        id: this.app!.id,
        app: updatedApp
      });
      this.$router.push("/main/admin/apps");
    }
  }

  get app() {
    return readAdminOneApp(this.$store)(+this.$router.currentRoute.params.id);
  }
}
</script>
