<template>
  <div>
    <v-container>
      <v-layout wrap>
        <v-flex>
          <v-select
            :items="langs"
            name="lang"
            label="Select a language"
            v-model="lang"
            item-text="name"
            return-object
            required
          ></v-select>
        </v-flex>
        <v-text-field label="Version" v-model="version"></v-text-field>
        <v-flex>
          <v-btn :color="color" @click="trigger">
            <slot>Choose File</slot>
          </v-btn>
          <input
            :multiple="multiple"
            class="visually-hidden"
            type="file"
            v-on:change="files"
            ref="fileInput"
          />
        </v-flex>
        <v-flex>
          <v-chip v-model="chip" close>{{ name }}</v-chip>
        </v-flex>
      </v-layout>
    </v-container>
  </div>
</template>

<script lang="ts">
import { Component, Vue, Prop, Emit } from "vue-property-decorator";
import { dispatchAddFile, dispatchGetLangs } from "../store/admin/actions";
import { readAdminLangs } from "../store/admin/getters";
import { IFileUpload, ILang } from "../interfaces";

@Component
export default class UploadLangFile extends Vue {
  public chip: boolean = false;
  public name: string = "";
  public lang: ILang = {};
  public version: string = "";
  public fileSelected: File | undefined;

  @Prop(String) public color: string | undefined;
  @Prop({ default: false }) public multiple!: boolean;

  public async files(e) {
    this.chip = true;
    this.fileSelected = e.target.files[0];
    if (this.fileSelected) {
      this.name = this.fileSelected.name;
      const fileUploadSelected: IFileUpload = {
        lang: this.lang,
        version: this.version,
        file: this.fileSelected
      };
      await dispatchAddFile(this.$store, fileUploadSelected);
    }
  }

  public reset() {
    this.name = "";
    this.version = "";
    this.lang = {} as any;
    this.$validator.reset();
  }

  public async mounted() {
    await dispatchGetLangs(this.$store);
    this.reset();
  }

  get langs() {
    return readAdminLangs(this.$store);
  }

  public trigger() {
    (this.$refs.fileInput as HTMLElement).click();
  }
}
</script>

<style scoped>
.visually-hidden {
  position: absolute !important;
  height: 1px;
  width: 1px;
  overflow: hidden;
  clip: rect(1px, 1px, 1px, 1px);
}
</style>
