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
import { readAdminOneLang } from "@/store/admin/getters";
import { ILangUpdate } from "../../../interfaces";
import { dispatchUpdateLang } from "../../../store/admin/actions";

@Component
export default class EditLang extends Vue {
  public valid = true;
  public name: string = "";

  public async mounted() {
    this.reset();
  }

  public reset() {
    this.name = "";
    this.$validator.reset();
    if (this.lang) {
      this.name = this.lang.name;
    }
  }

  public cancel() {
    this.$router.back();
  }

  public async submit() {
    if (await this.$validator.validateAll()) {
      const updatedLang: ILangUpdate = {};
      if (this.name) {
        updatedLang.name = this.name;
      }

      await dispatchUpdateLang(this.$store, {
        id: this.lang!.id,
        lang: updatedLang
      });
      this.$router.push("/main/admin/langs");
    }
  }

  get lang() {
    return readAdminOneLang(this.$store)(+this.$router.currentRoute.params.id);
  }
}
</script>
