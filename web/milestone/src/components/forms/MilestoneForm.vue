<template>
  <v-card>
    <v-card-title class="bg-primary">マイルストーン情報</v-card-title>

    <v-card-text>
      <v-container class="pt-8">
        <v-form>
          <v-row>
            <v-col>
              <v-text-field label="プロジェクト名" outlined clearable hide-details="auto"></v-text-field>
            </v-col>
          </v-row>
        </v-form>
      </v-container>
    </v-card-text>

    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn color="blue darken-1" text @click="close">Close</v-btn>
      <v-btn color="blue darken-1" text @click="save">Save</v-btn>
    </v-card-actions>
  </v-card>
</template>
<script>
import { mapGetters, mapActions } from 'vuex'
import MonthPicker from '@/components/MonthPicker'
export default {

  components: {
    MonthPicker,
  },

  data() {
    return {
    };
  },

  computed: {
    // ...mapGetters('gantt', ['getPjModel']),
  },

  mounted() {
    // this.sPjModel = {...this.getPjModel};
  },

  methods: {
    ...mapActions('gantt',['changePjModel']),

    close() {
      this.$emit('close');
    },

    save() {
    }
  }
};
</script>
<style>
.bg-primary {
  background-color: var(--v-primary-base) !important;
  color: white !important;
}
</style>