<template>
  <div>
    <v-toolbar light>
      <v-toolbar-title>
        Manage Apps
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn color="primary" to="/main/admin/apps/create">Create App</v-btn>
    </v-toolbar>
    <v-data-table :headers="headers" :items="apps">
      <template slot="items" slot-scope="props">
        <td>{{ props.item.name }}</td>
        <td>{{ props.item.description }}</td>
        <td class="justify-center layout px-0">
          <v-tooltip top>
            <span>Edit</span>
            <v-btn slot="activator" flat :to="{name: 'main-admin-apps-edit', params: {id: props.item.id}}">
              <v-icon>edit</v-icon>
            </v-btn>
          </v-tooltip>
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
import { dispatchGetApps } from '@/store/admin/actions';

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
    }
  ];
  get apps() {
    return readAdminApps(this.$store);
  }

  public async mounted() {
    await dispatchGetApps(this.$store);
  }
}
</script>
