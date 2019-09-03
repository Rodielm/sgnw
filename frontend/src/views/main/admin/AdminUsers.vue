<template>
  <div>
    <v-dialog v-model="dialog" persistent max-width="290">
      <v-card>
        <v-card-text>Are you sure you want to delete?</v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="green darken-1" flat @click="dialog = false">Cancel</v-btn>
          <v-btn color="green darken-1" flat @click="removeItem()">Ok</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-toolbar light>
      <v-toolbar-title>Manage Users</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn color="primary" to="/main/admin/users/create">Create User</v-btn>
    </v-toolbar>
    <v-data-table :headers="headers" :items="users">
      <template slot="items" slot-scope="props">
        <td>{{ props.item.username }}</td>
        <td>{{ props.item.email }}</td>
        <td>
          <v-icon v-if="props.item.isActive">checkmark</v-icon>
        </td>
        <td>
          <v-icon v-if="props.item.isAdmin">checkmark</v-icon>
        </td>
        <td>
          <v-tooltip bottom>
            <template v-slot:activator="{ on }">
              <v-icon small class="mr-2" @click="editItem(props.item.id)" v-on="on">edit</v-icon>
            </template>
            <span>Edit User</span>
          </v-tooltip>
          <v-tooltip bottom>
            <template v-slot:activator="{on}">
              <v-icon small @click="showRemoveItem(props.item.id)" v-on="on">delete</v-icon>
            </template>
            <span>delete</span>
          </v-tooltip>
        </td>
      </template>
    </v-data-table>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import { Store } from 'vuex';
import { IUserProfile } from '@/interfaces';
import { readAdminUsers } from '@/store/admin/getters';
import { dispatchGetUsers, dispatchRemoveUser } from '@/store/admin/actions';

@Component
export default class AdminUsers extends Vue {
  public headers = [
    {
      text: 'Name',
      sortable: true,
      value: 'name',
      align: 'left',
    },
    {
      text: 'Email',
      sortable: true,
      value: 'email',
      align: 'left',
    },
    {
      text: 'Is Active',
      sortable: true,
      value: 'isActive',
      align: 'left',
    },
    {
      text: 'Is Admin',
      sortable: true,
      value: 'isAdmin',
      align: 'left',
    },
    {
      text: 'Actions',
      value: 'id',
    },
  ];
  public dialog = false;
  public selected = 0;
  get users() {
    return readAdminUsers(this.$store);
  }

  public async mounted() {
    await dispatchGetUsers(this.$store);
  }

  public editItem(id) {
    this.$router.push({
      name: 'main-admin-users-edit',
      params: { id },
    });
  }

  public showRemoveItem(id) {
    this.dialog = true;
    this.selected = id;
  }

  public async removeItem() {
    await dispatchRemoveUser(this.$store, { id: this.selected });
    this.dialog = false;
  }
}
</script>
