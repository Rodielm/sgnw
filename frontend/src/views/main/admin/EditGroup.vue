<template>
  <v-container fluid>
    <v-card class="ma-3 pa-3">
      <v-card-title primary-title>
        <div class="headline primary--text">Edit Group</div>
      </v-card-title>
      <v-card-text>
        <template>
          <v-form v-model="valid" ref="form" lazy-validation>
            <v-text-field label="Name" v-model="name" required></v-text-field>
            <v-text-field label="Description" v-model="description" required></v-text-field>
            <v-layout align-center>
              <v-flex>
                <v-select
                  disabled
                  :items="apps"
                  name="app"
                  label="Select an app"
                  v-model="app"
                  item-text="name"
                  return-object
                ></v-select>
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
import { IApp, IGroupUpdate } from "@/interfaces";
import { dispatchUpdateGroup, dispatchGetGroups, dispatchCreateUser, dispatchGetApps } from "@/store/admin/actions";
import { readAdminOneGroup, readAdminApps } from "@/store/admin/getters";

@Component
export default class EditGroup extends Vue {
  public valid = true;
  public name: string = "";
  public description: string = "";
  public app: IApp = {} as any;

  public async mounted() {
    await dispatchGetGroups(this.$store);
    await dispatchGetApps(this.$store);
    this.reset();
  }

  public reset() {
    this.name = "";
    this.description = "";
    this.$validator.reset();
    if (this.group) {
      this.name = this.group.name;
      this.description = this.group.description;
      this.app = this.group.app
    }
  }

  public cancel() {
    this.$router.back();
  }

  public async submit() {
    if (await this.$validator.validateAll()) {
      const updatedGroup: IGroupUpdate = {};
      if (this.name) {
        updatedGroup.name = this.name;
      }
      if (this.description) {
        updatedGroup.description = this.description;
      }
      await dispatchUpdateGroup(this.$store, {
        id: this.group!.id,
        group: updatedGroup
      });
      this.$router.push("/main/admin/groups");
    }
  }

  get apps(){
    return readAdminApps(this.$store);
  }

  get group() {
    return readAdminOneGroup(this.$store)(+this.$router.currentRoute.params.id);
  }
}
</script>
