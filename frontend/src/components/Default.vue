<template>
  <div class="hello">
    <b-card
      header="오늘 해야 할 일"
      style="max-width: 40rem; margin: auto; margin-top: 10vh"
      class="mb-2"
      border-variant="info"
      align="left"
    >
      <b-form-group id="to-do-input">
        <b-container fluid>
          <b-row class="my-1">
            <b-col sm="10">
              <b-form-input
                type="text"
                placeholder="새 할 일을 적으세요."
              />
            </b-col>
            <b-col sm="2">
              <b-button variant="outline-primary">추가</b-button>
            </b-col>
          </b-row>
        </b-container>
      </b-form-group>

      <b-list-group>
        <b-list-group-item
        >
          <b-form-checkbox >
          </b-form-checkbox>
        </b-list-group-item>
      </b-list-group>
    </b-card>
  </div>
</template>

<script>

export default {
  name: 'hello',
};
</script>
