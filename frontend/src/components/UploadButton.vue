<template>
  <div>
    <v-btn :color="color" @click="trigger">
      <slot>Choose File</slot>
    </v-btn>
  </div>
</template>

<script lang="ts">
import { Component, Vue, Prop, Emit } from "vue-property-decorator";

@Component
export default class UploadButton extends Vue {
  @Prop(String) public color: string | undefined;
  @Prop({ default: false }) public multiple!: boolean;
  @Emit()
  public async files(e) {
    console.log(e.target.files[0]);
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
