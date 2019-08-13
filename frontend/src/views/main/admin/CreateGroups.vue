<template>
  <v-container fluid>
    <v-card class="ma-3 pa-3">
      <v-card-title primary-title>
        <div class="headline primary--text">Create Group</div>
      </v-card-title>
      <v-card-text>
        <template>
          <v-form v-model="valid" ref="form" lazy-validation>
            <v-text-field label="Name" v-model="name" required></v-text-field>
            <v-text-field label="Description" v-model="description"></v-text-field>
            <v-layout align-center>
              <v-flex>
                <v-select :items="apps" label="App">
                </v-select>
              </v-flex>
            </v-layout>
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
import {
  IGroups,
  IGroupsCreate
} from "@/interfaces";
// import { readAdminApps } from '@/store/admin/getters';
import { dispatchGetGroups, dispatchCreateGroups } from "@/store/admin/actions";

@Component
export default class CreateGroup extends Vue {
  public valid = false;
  public name: string = "";
  public description: string = "";
  public app: number = 0;
  
  public async mounted() {
    await dispatchGetGroups(this.$store);
    this.reset();
  }

  // get apps(){
  //   return readAdminApps(this.$store);
  // }

  public reset() {
    this.name = "";
    this.description = "";
    this.app = 0;
    this.$validator.reset();
  }

  public cancel() {
    this.$router.back();
  }

  public async submit() {
    if (await this.$validator.validateAll()) {
      const updatedGroup: IGroupsCreate = {
        name: this.name
      };
      if (this.description) {
        updatedGroup.description = this.description;
      }
      if (this.name) {
        updatedGroup.name = this.name;
      }
      if(this.app){
        updatedGroup.app = this.app
      }
      await dispatchCreateGroups(this.$store, updatedGroup);
      this.$router.push("/main/admin/groups");
    }
  }
}
</script>
