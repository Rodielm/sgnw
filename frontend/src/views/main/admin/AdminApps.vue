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
      <v-toolbar-title>Manage Apps</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn color="primary" to="/main/admin/apps/create">Create App</v-btn>
    </v-toolbar>
    <v-data-table :headers="headers" :items="apps">
      <template slot="items" slot-scope="props">
        <td>{{ props.item.name }}</td>
        <td>{{ props.item.description }}</td>
        <td>
          <span v-for="(l,index) in props.item.appLangs" :key="l.id">
            <span>{{l.lang.name}}</span>
            <span v-if="index+1 < props.item.appLangs.length">,</span>
          </span>
        </td>
        <td>
          <v-icon small class="mr-2" @click="editItem(props.item.id)">edit</v-icon>
          <v-icon small @click="showRemoveItem(props.item.id)">delete</v-icon>
        </td>
      </template>
    </v-data-table>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import { Store } from 'vuex';
import { IApp } from '@/interfaces';
import { readAdminApps } from '@/store/admin/getters';
import { dispatchGetApps, dispatchRemoveApp } from '@/store/admin/actions';

@Component
export default class AdminApps extends Vue {
  public headers = [
    {
      text: 'Name',
      sortable: true,
      value: 'name',
      align: 'left',
    },
    {
      text: 'Description',
      sortable: true,
      value: 'description',
      align: 'left',
    },
    {
      text: 'Languages',
      sortable: true,
      value: 'lang',
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
  get apps() {
    return readAdminApps(this.$store);
  }

  public editItem(id) {
    this.$router.push({
      name: 'main-admin-apps-edit',
      params: { id },
    });
  }

  public async mounted() {
    await dispatchGetApps(this.$store);
  }

  public showRemoveItem(id) {
    this.dialog = true;
    this.selected = id;
  }

  public async removeItem(id) {
    await dispatchRemoveApp(this.$store, { id: this.selected });
    this.dialog = false;
  }
}
</script>
