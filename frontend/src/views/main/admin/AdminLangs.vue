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
      <v-toolbar-title>Manage Lang</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn color="primary" to="/main/admin/langs/create">Create Lang</v-btn>
    </v-toolbar>
    <v-data-table :headers="headers" :items="langs">
      <template slot="items" slot-scope="props">
        <td>{{ props.item.name }}</td>
        <td>
          <v-tooltip bottom>
            <template v-slot:activator="{ on }">
              <v-icon small class="mr-2" @click="editItem(props.item.id)" v-on="on">edit</v-icon>
            </template>
            <span>Edit Lang</span>
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
import { readAdminLangs } from '@/store/admin/getters';
import { dispatchGetLangs, dispatchRemoveLang } from '@/store/admin/actions';

@Component
export default class AdminLangs extends Vue {
  public headers = [
    {
      text: 'Name',
      sortable: true,
      value: 'name',
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
  get langs() {
    return readAdminLangs(this.$store);
  }

  public async mounted() {
    await dispatchGetLangs(this.$store);
  }

  public editItem(id) {
    this.$router.push({
      name: 'main-admin-langs-edit',
      params: { id },
    });
  }

  public showRemoveItem(id) {
    this.dialog = true;
    this.selected = id;
  }

  public async removeItem(id) {
    await dispatchRemoveLang(this.$store, { id: this.selected });
    this.dialog = false;
  }
}
</script>
