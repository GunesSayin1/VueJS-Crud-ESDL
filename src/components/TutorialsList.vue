<template>
  <a-table
    :columns="columns"
    :row-key="(record) => record.id"
    :data-source="data"
  >
    <template #id="{ text}">
      <router-link :to="'/ESDLs/' + text">{{ text }}</router-link>
    </template>

    <template #published="{ text: tags }">
      <span>
        <a-tag :key="tag" :color="tags === 'False' ? 'volcano' : 'green'">
          {{ tags.toUpperCase() }}
        </a-tag>
      </span>
    </template>
  </a-table>
</template>
<script>
import ESDLDataService from "../services/ESDLDataService";

const columns = [
  {
    title: "Id",
    dataIndex: "id",
    sorter: true,
    width: "20%",
    slots: {
      customRender: "id",
    },
  },
  {
    title: "Title",
    dataIndex: "title",
  },
  {
    title: "Description",
    dataIndex: "description",
  },
  {
    title: "Simulated",
    dataIndex: "published",
    slots: {
      customRender: "published",
    },
  },
];

export default {
  data() {
    return {
      data: [],
      loading: false,
      columns,
    };
  },
  mounted() {
    this.retriveESDLs();
  },
  methods: {
    retriveESDLs() {
      ESDLDataService.getAll()
        .then((response) => {
          this.data = response.data.ESDLs;
          console.log(response.data.ESDLs);
        })
        .catch((e) => {
          console.log(e);
        });
    },
  },
};
</script>
