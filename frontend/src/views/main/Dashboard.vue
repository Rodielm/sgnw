<template>
  <v-container fluid>
    <v-dialog v-model="dialog" max-width="500px">
      <v-card>
        <v-card-title
          class="headline grey lighten-2"
          primary-title
        >{{selectedItem.notification? selectedItem.notification.summary:""}}</v-card-title>
        <v-card-text>{{selectedItem.notification? selectedItem.notification.body:""}}</v-card-text>
        <v-divider></v-divider>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary" flat @click="dialog = false">Ok</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-card class="ma-3 pa-3">
      <v-card-title primary-title>
        <div class="headline primary--text">Notifications</div>
      </v-card-title>
      <v-card-text>
        <div v-if="selected.length">
          <v-icon class="mr-2">drafts</v-icon>
          <v-icon>delete</v-icon>
        </div>
        <v-text-field v-model="search" append-icon="search" label="Search" single-line hide-details></v-text-field>
        <v-data-table v-model="selected" :headers="headers" :search="search" select-all :items="userNotifies">
          <template v-slot:headers="props">
            <tr>
              <th>
                <v-checkbox
                  :input-value="props.all"
                  :indeterminate="props.indeterminate"
                  primary
                  hide-details
                  @click.stop="toggleAll"
                ></v-checkbox>
              </th>
              <th v-for="header in props.headers" :key="header.text">
                <v-icon small>arrow_upward</v-icon>
                {{header.text}}
              </th>
            </tr>
          </template>
          <template v-slot:items="props">
            <td :active="props.selected" @click="propSelectedRow(props)">
              <v-checkbox :input-value="props.selected" primary hide-details></v-checkbox>
            </td>
            <td
              :style="{fontWeight:(props.item.status.name == 'Nuevo'?'bold':'400')}"
            >{{ props.item.notification.summary + ' ' + props.item.id }}</td>
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
              <v-tooltip bottom>
                <template v-slot:activator="{ on }">
                  <v-icon
                    small
                    class="mr-2"
                    @click.stop="showNotifyUser(props.item,true)"
                    v-on="on"
                  >remove_red_eye</v-icon>
                </template>
                <span>Show notification</span>
              </v-tooltip>
              <v-tooltip bottom>
                <template v-slot:activator="{on}">
                  <v-icon
                    small
                    class="mr-2"
                    @click="showNotifyUser(props.item,false)"
                    v-on="on"
                  >drafts</v-icon>
                </template>
                <span>Mark read</span>
              </v-tooltip>
              <v-tooltip bottom>
                <template v-slot:activator="{on}">
                  <v-icon small @click="deleteNotifyUser(props.item)" v-on="on">delete</v-icon>
                </template>
                <span>delete</span>
              </v-tooltip>
            </td>
          </template>
        </v-data-table>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import { Store } from 'vuex';
import {
  readUserProfile,
  readUsersNotify,
  readOneUsersNotify,
} from '@/store/main/getters';
import {
  dispatchUserNotify,
  dispatchUpdateUserNotifyStatus,
  dispatchRemoveUserNotifyStatus,
} from '../../store/main/actions';
import { INotifyUser } from '../../interfaces';

@Component
export default class Dashboard extends Vue {
  public dialog: boolean = false;
  public selectedItem: INotifyUser = { id: 0 };
  public selected: any[] = [];
  public search: string = '';
  public headers = [
    {
      text: 'Summary',
      sortable: true,
      value: 'name',
      align: 'left',
    },
    {
      text: 'Notification',
      sortable: true,
      value: 'description',
      align: 'left',
    },
    {
      text: 'Groups',
      sortable: true,
      value: 'group',
      align: 'left',
    },
    {
      text: 'Roles',
      sortable: true,
      value: 'rol',
      align: 'left',
    },
    {
      text: 'Actions',
      value: 'id',
      align: 'left',
    },
  ];
  public async mounted() {
    await dispatchUserNotify(this.$store);
  }

  public toggleAll() {
    if (this.selected.length) {
      this.selected = [];
    } else {
      this.selected = this.userNotifies.slice();
    }
  }

  public propSelectedRow(props) {
    props.selected = !props.selected;
  }

  public async showNotifyUser(selectedItem, showOnDialog: boolean) {
    this.selectedItem = Object.assign({}, selectedItem);
    if (selectedItem.status.name === 'Nuevo') {
      dispatchUpdateUserNotifyStatus(this.$store, {
        idNoti: this.selectedItem!.id,
        idStatus: 2,
      });
    }
    if (showOnDialog) {
      this.dialog = true;
    }
  }

  public async deleteNotifyUser(selectedItem) {
    this.selectedItem = Object.assign({}, selectedItem);
    dispatchRemoveUserNotifyStatus(this.$store, {
      idNoti: this.selectedItem!.id,
      idStatus: 3,
    });
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
