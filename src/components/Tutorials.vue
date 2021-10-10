<template>
  <a-row type="flex" justify="center" align="top">
    <a-card
      :title="'ESDL' + ' ' + currentESDL.id"
      justify="center"
      :bordered="false"
      style="width: 750px"
    >
      <template #extra>
        <DeleteOutlined
          :style="{ fontSize: '24px', color: '#08c' }"
          @click="deleteESDL"
        />
      </template>
      <a-row>
        <a-col :span="8">
          <h3><span>ESDL Title:</span> {{ currentESDL.title }}</h3>

          <h3><span>ESDL Description:</span> {{ currentESDL.description }}</h3>
        </a-col>
        <a-col :span="8" style="display: inline-block">
          <a-input v-model:value="title" placeholder="New Title" />
          <a-input v-model:value="description" placeholder="New Description" />
          <br /><br />
          <a-checkbox v-model:checked="published">Publish</a-checkbox>
        </a-col>
        <a-col :span="8" align="middle">
          <a-tag :color="currentESDL.published === false ? 'volcano' : 'green'">
            <p v-if="currentESDL.published === false">Not Published</p>
            <p v-else-if="currentESDL.published === true">Published</p>
          </a-tag>
        </a-col>
      </a-row>
      <br />
      <a-row type="flex" justify="center" align="middle">
        <a-col>
          <a-button @click="updateESDL">Update</a-button>
        </a-col>
      </a-row>
    </a-card>
  </a-row>
  <a-row type="flex" justify="center" align="top">
    <a-card :title="'ESDL File in JSON Format'" justify="center">
      <vue-json-pretty
        :path="'res'"
        :data="currentESDL.file"
        :deep="1"
      ></vue-json-pretty>
    </a-card>
  </a-row>
</template>

<script>
import ESDLDataService from "../services/ESDLDataService";
import { DeleteOutlined } from "@ant-design/icons-vue";
import { message } from "ant-design-vue";
import VueJsonPretty from "vue-json-pretty";
import "vue-json-pretty/lib/styles.css";
export default {
  components: {
    DeleteOutlined,
    VueJsonPretty,
  },
  data() {
    return {
      currentESDL: {},
      title: "",
      description: "",
      published: false,
      text: "",
    };
  },
  mounted() {
    this.getESDL(this.$route.params.id);
  },
  methods: {
    getESDL(id) {
      ESDLDataService.get(id).then((response) => {
        this.currentESDL = response.data.ESDL;
        const esdl_string = atob(this.currentESDL.file);
        this.currentESDL.file = JSON.parse(esdl_string);
      });
    },
    deleteESDL() {
      ESDLDataService.delete(this.currentESDL.id).then((response) => {
        message.warning(response.data.message, 2);
        this.$router.push("/");
      });
    },
    updateESDL() {
      ESDLDataService.update(this.currentESDL.id, {
        title: this.title,
        description: this.description,
        published: this.published,
      }).then((response) => {
        console.log(this.published);
        message.success(response.data.message, 2);
        this.$router.go(-1);
      });
    },
  },
};
</script>

<style lang="scss" scoped>
h3 {
  color: rgb(201, 125, 39);
  span {
    color: #42b883;
  }
}
</style>
