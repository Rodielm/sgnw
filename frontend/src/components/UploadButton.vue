<template>
  <div>
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
    <v-chip v-model="chip" close>{{ name }}</v-chip>
  </div>
</template>

<script lang="ts">
import { Component, Vue, Prop, Emit } from "vue-property-decorator";
import { dispatchAddFile } from "../store/admin/actions";

@Component
export default class UploadButton extends Vue {
  public chip: boolean = false;
  public name: string = "";
  public fileSelected: File | undefined;

  @Prop(String) public color: string | undefined;
  @Prop({ default: false }) public multiple!: boolean;

  public async files(e) {
    this.chip = true;
    this.fileSelected = e.target.files[0];
    if (this.fileSelected) {
      this.name = this.fileSelected.name;
      await dispatchAddFile(this.$store, this.fileSelected);
    }
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
