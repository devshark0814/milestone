<template>
  <div>
    <v-card>
      <v-card-text>
        <v-row>
          <v-spacer />
          <v-col cols="3">
            <div style="display:flex">
              <v-text-field
                outlined
                placeholder="Search User"
                hide-details
                dense
                class="mr-2"
              >
              </v-text-field>
              <v-btn
                depressed
                color="primary"
                class="mt-1"
              >
                新規追加
              </v-btn>
            </div>
          </v-col>
        </v-row>
      </v-card-text>
      <v-data-table
        :headers="headers"
        :items="desserts"
        class="elevation-1"
        @click:row="userDialog = true"
      >
      </v-data-table>
    </v-card>
    <UserDialog :dialog="userDialog"/>
  </div>
</template>
<script>
import UserDialog from '@/components/UserDialog.vue';
export default {
  components: {
    UserDialog
  },
  data() {
    return {
      headers: [
        { text: 'id', value: 'id' },
        { text: '氏名', value: 'name' },
      ],
      desserts: [
        { id: 1, name: 'AAA' },
        { id: 2, name: 'BBB' },
        { id: 3, name: 'CCC' },
      ],
      userDialog: false,
    }
  },

  method: {
  }
}
</script>