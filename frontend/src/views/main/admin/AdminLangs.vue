<template>
  <div>
    <v-toolbar light>
      <v-toolbar-title>Manage Lang</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn color="primary" to="/main/admin/langs/create">Create Lang</v-btn>
    </v-toolbar>
    <v-data-table :headers="headers" :items="langs">
      <template slot="items" slot-scope="props">
        <td>{{ props.item.name }}</td>

        <td class="justify-center layout px-0">
          <v-tooltip top>
            <span>Edit</span>
            <v-btn
              slot="activator"
              flat
              :to="{name: 'main-admin-langs-edit', params: {id: props.item.id}}"
            >
              <v-icon>edit</v-icon>
            </v-btn>
          </v-tooltip>
        </td>
      </template>
    </v-data-table>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import { Store } from "vuex";
import { readAdminLangs } from "@/store/admin/getters";
import { dispatchGetLangs } from "@/store/admin/actions";

@Component
export default class AdminLangs extends Vue {
  public headers = [
    {
      text: "Name",
      sortable: true,
      value: "name",
      align: "left"
    }
  ];
  get langs() {
    return readAdminLangs(this.$store);
  }

  public async mounted() {
    await dispatchGetLangs(this.$store);
  }
}
</script>
