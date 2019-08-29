<template>
  <div>
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
          <span v-for="(l,index) in props.item.app_langs" :key="l.id">
            <span>{{l.lang.name}}</span>
            <span v-if="index+1 < props.item.app_langs.length">, </span>
          </span>
        </td>
        <td>
          <v-icon small class="mr-2" @click="editItem(props.item.id)">edit</v-icon>
          <v-icon small @click="deleteItem(props.item.id)">delete</v-icon>
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
}
</script>
