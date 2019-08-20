<template>
  <v-container fluid>
    <v-card class="ma-3 pa-3">
      <v-card-title primary-title>
        <div class="headline primary--text">Edit Role</div>
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
import { IApp, IRoleUpdate } from "@/interfaces";
import { dispatchGetApps, dispatchGetRoles, dispatchUpdateRole } from "@/store/admin/actions";
import { readAdminApps, readAdminOneRole } from "@/store/admin/getters";

@Component
export default class EditRole extends Vue {
  public valid = true;
  public name: string = "";
  public description: string = "";
  public app: IApp = {} as any;

  public async mounted() {
    await dispatchGetRoles(this.$store);
    await dispatchGetApps(this.$store);
    this.reset();
  }

  public reset() {
    this.name = "";
    this.description = "";
    this.$validator.reset();
    if (this.role) {
      this.name = this.role.name;
      this.description = this.role.description;
      this.app = this.role.app
    }
  }

  public cancel() {
    this.$router.back();
  }

  public async submit() {
    if (await this.$validator.validateAll()) {
      const updateRole: IRoleUpdate = {};
      if (this.name) {
        updateRole.name = this.name;
      }
      if (this.description) {
        updateRole.description = this.description;
      }
      await dispatchUpdateRole(this.$store, {
        id: this.role!.id,
        role: updateRole
      });
      this.$router.push("/main/admin/roles");
    }
  }

  get apps(){
    return readAdminApps(this.$store);
  }

  get role() {
    return readAdminOneRole(this.$store)(+this.$router.currentRoute.params.id);
  }
}
</script>
