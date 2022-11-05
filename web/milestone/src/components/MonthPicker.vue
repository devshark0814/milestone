<template>
  <v-menu ref="menu" v-model="menu" :close-on-content-click="false" :return-value.sync="date"
    transition="scale-transition" offset-y max-width="290px" min-width="auto">

    <template v-slot:activator="{ on, attrs }">
      <v-text-field v-model="date" outlined :label="label" prepend-inner-icon="mdi-calendar" readonly v-bind="attrs" v-on="on">
      </v-text-field>
    </template>

    <v-date-picker v-model="date" locale="jp-ja" no-title scrollable>
      <v-spacer></v-spacer>
      <v-btn text color="primary" @click="menu = false">
        Cancel
      </v-btn>
      <v-btn text color="primary" @click="$refs.menu.save(date)">
        OK
      </v-btn>
    </v-date-picker>

  </v-menu>
</template>
<script>
export default {

  props: {
    value: {
      type: String,
      default: new Date().toISOString().substr(0, 10),
    },
    label: {
      type: String,
      default: '',
    }
  },

  computed: {
    date: {
      get() {
        return new Date(this.value).toISOString().substr(0, 10)
      },
      set(v) {
        this.$emit('input', v)
      }
    }
  },

  data() {
    return {
      menu: false,
    }
  }
}
</script>