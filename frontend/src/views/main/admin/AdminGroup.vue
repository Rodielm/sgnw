<template>
  <div>
    <v-toolbar light>
      <v-toolbar-title>
        Manage Groups
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn color="primary" to="/main/admin/groups/create">Create Group</v-btn>
    </v-toolbar>
    <v-data-table :headers="headers" :items="groups">
      <template slot="items" slot-scope="props">
        <td>{{ props.item.name }}</td>
        <td>{{ props.item.app }}</td>
        <td class="justify-center layout px-0">
          <v-tooltip top>
            <span>Edit</span>
            <v-btn slot="activator" flat :to="{name: 'main-admin-groups-edit', params: {idGroup: props.item.id, idApp: props.item.idApp}}">
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
import { IGroups } from '@/interfaces';
import { readAdminGroups } from '@/store/admin/getters';
import { dispatchGetGroups } from '@/store/admin/actions';

@Component
export default class AdminGroups extends Vue {
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
    }
  ];
  get groups() {
    return readAdminGroups(this.$store);
  }

  public async mounted() {
    await dispatchGetGroups(this.$store);
  }
}
</script>
