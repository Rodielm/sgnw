<template>
  <v-container fluid>
    <v-card class="ma-3 pa-3">
      <v-card-title primary-title>
        <div class="headline primary--text">Dashboard</div>
      </v-card-title>
      <v-card-text>
        <div class="headline font-weight-light ma-5">Welcome {{greetedUser}}</div>
        <v-data-table :headers="headers" :items="userNotifies">
          <template v-slot:items="props">
            <tr @click="props.expanded = !props.expanded">
              <td
                :style="{fontWeight:(props.item.status.name == 'Nuevo'?'bold':'400')}"
              >{{ props.item.notification.summary }}</td>
              <td
                :style="{fontWeight:(props.item.status.name == 'Nuevo'?'bold':'400')}"
              >{{ props.item.notification.body }}</td>
              <td :style="{fontWeight:(props.item.status.name == 'Nuevo'?'bold':'400')}">
                <span v-for="(g,index) in props.item.groups" :key="g.id">
                  <span>{{g.name}}</span>
                  <span v-if="index+1 < props.item.groups.length">,</span>
                </span>
              </td>
              <td :style="{fontWeight:(props.item.status.name == 'Nuevo'?'bold':'400')}">
                <span v-for="(g,index) in props.item.roles" :key="g.id">
                  <span>{{g.name}}</span>
                  <span v-if="index+1 < props.item.roles.length">,</span>
                </span>
              </td>
              <td>
                <v-icon small class="mr-2">remove_red_eye</v-icon>
                <v-icon small class="mr-2" @click="editItem(props.item.id)">edit</v-icon>
                <v-icon small @click="deleteItem(props.item.id)">delete</v-icon>
              </td>
            </tr>
          </template>
          <template v-slot:expand="props">
            <v-card flat>
              <v-card-text>{{props.item.notification.body}}</v-card-text>
            </v-card>
          </template>
        </v-data-table>
      </v-card-text>
      <v-card-actions>
        <v-btn to="/main/profile/view">View Profile</v-btn>
        <v-btn to="/main/profile/edit">Edit Profile</v-btn>
        <v-btn to="/main/profile/password">Change Password</v-btn>
      </v-card-actions>
    </v-card>
  </v-container>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import { Store } from "vuex";
import { readUserProfile, readUsersNotify } from "@/store/main/getters";
import { dispatchUserNotify } from "../../store/main/actions";

@Component
export default class Dashboard extends Vue {
  public expand = true;
  public headers = [
    {
      text: "Summary",
      sortable: true,
      value: "name",
      align: "left"
    },
    {
      text: "Notification",
      sortable: true,
      value: "description",
      align: "left"
    },
    {
      text: "Groups",
      sortable: true,
      value: "group",
      align: "left"
    },
    {
      text: "Roles",
      sortable: true,
      value: "rol",
      align: "left"
    },
    {
      text: "Actions",
      value: "id",
      align: "left"
    }
  ];
  public async mounted() {
    await dispatchUserNotify(this.$store);
  }

  get greetedUser() {
    const userProfile = readUserProfile(this.$store);
    if (userProfile && userProfile.username) {
      if (userProfile.username) {
        return userProfile.username;
      } else {
        return userProfile.email;
      }
    }
  }

  get userNotifies() {
    return readUsersNotify(this.$store);
  }
}
</script>
