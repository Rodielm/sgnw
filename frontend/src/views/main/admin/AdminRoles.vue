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
      <v-toolbar-title>Manage Roles</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn color="primary" to="/main/admin/roles/create">Create Role</v-btn>
    </v-toolbar>
    <v-data-table :headers="headers" :items="roles">
      <template slot="items" slot-scope="props">
        <td>{{ props.item.name }}</td>
        <td>{{ props.item.app? props.item.app.name:''}}</td>
        <td>
          <v-tooltip bottom>
            <template v-slot:activator="{ on }">
              <v-icon small class="mr-2" @click="editItem(props.item.id)" v-on="on">edit</v-icon>
            </template>
            <span>Edit Role</span>
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
import { IRole } from '@/interfaces';
import { readAdminRoles } from '@/store/admin/getters';
import { dispatchGetRoles, dispatchRemoveRole } from '@/store/admin/actions';

@Component
export default class AdminRoles extends Vue {
  public headers = [
    {
      text: 'Name',
      sortable: true,
      value: 'name',
      align: 'left',
    },
    {
      text: 'App',
      sortable: true,
      value: 'app',
      align: 'left',
    },
    {
      text: 'Actions',
      value: 'id',
      align: 'left',
    },
  ];
  public dialog = false;
  public selected = 0;
  get roles() {
    return readAdminRoles(this.$store);
  }

  public async mounted() {
    await dispatchGetRoles(this.$store);
  }

  public editItem(id) {
    this.$router.push({
      name: 'main-admin-roles-edit',
      params: { id },
    });
  }

  public showRemoveItem(id) {
    this.dialog = true;
    this.selected = id;
  }

  public async removeItem(id) {
    await dispatchRemoveRole(this.$store, { id: this.selected });
    this.dialog = false;
  }
}
</script>
