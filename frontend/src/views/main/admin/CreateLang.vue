<template>
  <v-container fluid>
    <v-card class="ma-3 pa-3">
      <v-card-title primary-title>
        <div class="headline primary--text">Create Lang</div>
      </v-card-title>
      <v-card-text>
        <template>
          <v-form v-model="valid" ref="form" lazy-validation>
            <v-text-field label="Name" v-model="name" required></v-text-field>
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
import { IApp, IAppCreate, ILangCreate } from "@/interfaces";
import { readAdminApps } from "@/store/admin/getters";
import { dispatchGetApps, dispatchCreateApp, dispatchCreateUser, dispatchCreateLang } from "@/store/admin/actions";

@Component
export default class CreateLang extends Vue {
  public valid = false;
  public name: string = "";

  public async mounted() {
    this.reset();
  }

  public reset() {
    this.name = "";
    this.$validator.reset();
  }

  public cancel() {
    this.$router.back();
  }

  public async submit() {
    if (await this.$validator.validateAll()) {
      const updatedLang: ILangCreate = {
        name: this.name
      };
      if (this.name) {
        updatedLang.name = this.name;
      }
      await dispatchCreateLang(this.$store, updatedLang);
      this.$router.push("/main/admin/langs");
    }
  }
}
</script>
