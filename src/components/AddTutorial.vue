<template>
  <div class="sign-in">
    <a-row
      type="flex"
      :gutter="[24, 24]"
      justify="space-around"
      align="middle"
      style="margin-top: 10px"
    >
      <a-col
        :span="24"
        :md="12"
        :lg="{ span: 12, offset: 0 }"
        :xl="{ span: 6, offset: 2 }"
        class="col-form"
      >
        <a-form
          :model="formState"
          :label-col="labelCol"
          :wrapper-col="wrapperCol"
        >
          <a-form-item label="Title">
            <a-input v-model:value="formState.title" />
          </a-form-item>
          <a-form-item label="Description">
            <a-input v-model:value="formState.description" type="textarea" />
          </a-form-item>
          <a-form-item label="File">
            <div class="clearfix">
              <a-upload
                :file-list="fileList"
                :remove="handleRemove"
                :before-upload="beforeUpload"
              >
                <a-button>
                  <upload-outlined />
                  Select File
                </a-button>
              </a-upload>
              <a-button
                type="primary"
                :loading="uploading"
                :disabled="fileList.length === 0"
                style="margin-top: 16px"
                @click="handleUpload"
              >
                {{ uploading ? "Uploading" : "Start Upload" }}
              </a-button>
            </div>
          </a-form-item>
        </a-form>
      </a-col>
      <!-- Sign In Image Column -->
    </a-row>
  </div>
</template>
<script>
import { defineComponent, reactive, ref } from "vue";
import router from "../router";
import { UploadOutlined } from "@ant-design/icons-vue";
import { message } from "ant-design-vue";
import ESDLDataService from "../services/ESDLDataService";
export default defineComponent({
  components: {
    UploadOutlined,
  },
  setup() {
    const fileList = ref([]);
    const esdl_file = ref("");
    const uploading = ref(false);
    const formState = reactive({
      title: "",
      description: "",
      published: false,
      file: "",
    });

    const onSubmit = () => {
      var data = {
        title: formState.title,
        description: formState.description,
        published: false,
        file: esdl_file.value,
      };

      ESDLDataService.create(data)
        .then((response) => {
          console.log(response.data.message);
          message.success(response.data.message, 2);
          router.push("/");
        })
        .catch((e) => {
          console.log(e);
        });
    };

    const handleRemove = (file) => {
      const index = fileList.value.indexOf(file);
      const newFileList = fileList.value.slice();
      newFileList.splice(index, 1);
      fileList.value = newFileList;
    };

    const beforeUpload = (file) => {
      fileList.value = [...fileList.value, file];
      return false;
    };
    const handleUpload = () => {
      const formData = new FormData();
      fileList.value.forEach((file) => {
        formData.append("files[]", file);
      });
      printFile(fileList.value[0]);

      uploading.value = true;
    };

    function printFile(file) {
      const reader = new FileReader();
      reader.onload = function(evt) {
        esdl_file.value = btoa(evt.target.result);
      };
      reader.readAsText(file);
      reader.onloadend = () => onSubmit();
      uploading.value = false;
    }

    return {
      labelCol: {
        style: {
          width: "120px",
        },
      },
      wrapperCol: {
        span: 14,
      },
      formState,
      onSubmit,
      handleUpload,
      handleRemove,
      beforeUpload,
      uploading,
      fileList,
    };
  },
});
</script>
