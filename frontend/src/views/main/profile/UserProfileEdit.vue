<template>
  <v-container fluid>
    <v-card class="ma-3 pa-3">
      <v-card-title primary-title>
        <div class="headline primary--text">Edit User Profile</div>
      </v-card-title>
      <v-card-text>
        <template>
          <!-- <div class="my-3">
            <div class="subheading secondary--text text--lighten-2">Username</div>
            <div class="title primary--text text--darken-2" v-if="user">{{user.email}}</div>
            <div class="title primary--text text--darken-2" v-else>-----</div>
          </div>-->
          <v-form v-model="valid" ref="form" lazy-validation>
            <v-text-field label="Full Name" v-model="fullName" required></v-text-field>
            <v-text-field
              label="E-mail"
              type="email"
              v-model="email"
              v-validate="'required|email'"
              data-vv-name="email"
              :error-messages="errors.collect('email')"
              required
            ></v-text-field>
            <div class="subheading secondary--text text--lighten-2">User notification settings</div>
            <v-radio-group v-model="markAllReadOrDelete">
              <v-radio label="Mark all as read" value="2"></v-radio>
              <v-radio label="Mark all as deleted" value="3"></v-radio>
            </v-radio-group>
            <v-checkbox label="Send all by mail" v-model="sendAllByEmail"></v-checkbox>
            <v-select
              :items="langs"
              name="lang"
              label="Select a language"
              v-model="lang"
              item-text="name"
              return-object
              required
            ></v-select>
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
import { Store } from 'vuex';
import { IUserProfileUpdate } from '@/interfaces';
import { readUserProfile } from '@/store/main/getters';
import { dispatchUpdateUserProfile } from '@/store/main/actions';
import { dispatchGetLangs } from '../../../store/admin/actions';
import { readAdminLangs } from '../../../store/admin/getters';

@Component
export default class UserProfileEdit extends Vue {
  public valid = true;
  public fullName: string = '';
  public email: string = '';
  public isActive: boolean = false;
  public isSuperuser: boolean = false;
  public setPassword = false;
  public password1: string = '';
  public password2: string = '';
  public markAllReadOrDelete = '';
  public sendAllByEmail = '';
  public languagePreference = '';

  public created() {
    const userProfile = readUserProfile(this.$store);
    if (userProfile) {
      this.fullName = userProfile.username;
      this.email = userProfile.email;
    }
  }

  public async mounted() {
    await dispatchGetLangs(this.$store);
    this.reset();
  }

   get langs() {
    return readAdminLangs(this.$store);
  }

  get userProfile() {
    return readUserProfile(this.$store);
  }

  public reset() {
    const userProfile = readUserProfile(this.$store);
    if (userProfile) {
      this.fullName = userProfile.username;
      this.email = userProfile.email;
    }
  }

  public cancel() {
    this.$router.back();
  }

  public async submit() {
    if ((this.$refs.form as any).validate()) {
      const updatedProfile: IUserProfileUpdate = {};
      if (this.fullName) {
        updatedProfile.username = this.fullName;
      }
      if (this.email) {
        updatedProfile.email = this.email;
      }
      await dispatchUpdateUserProfile(this.$store, updatedProfile);
      this.$router.push('/main/profile');
    }
  }
}
</script>
