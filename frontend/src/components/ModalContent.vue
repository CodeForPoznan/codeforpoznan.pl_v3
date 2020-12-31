<template>
  <section class="modal">
    <div class="modal__title">
      <h2>{{ selectedProject.name }}</h2>
      <div class="modal__button-close" @click="onClick">
        <i class="fas fa-times"></i>
      </div>
    </div>
    <div class="modal__list">
      <a
        v-show="selectedProject.licensePage !== ''"
        class="btn-transparent"
        :href="selectedProject.licensePage"
        target="blank"
      >
        <i class="far fa-copyright btn-icon"></i>
        <span>Licencja</span>
      </a>
      <a
        v-show="selectedProject.githubLink !== ''"
        class="btn-transparent"
        :href="selectedProject.githubLink"
        target="blank"
      >
        <i class="fab fa-github btn-icon"></i>
        <span>Repozytorium</span>
      </a>
      <a
        v-show="selectedProject.websiteLink !== ''"
        class="btn-transparent"
        :href="selectedProject.websiteLink"
        target="blank"
      >
        <i class="fas fa-globe btn-icon"></i>
        <span>Strona projektu</span>
      </a>
    </div>
    <div class="modal__description">
      <p class="text-center">{{ selectedProject.description }}</p>
    </div>
    <div v-show="countPartners > 0">
      <div class="modal__title">
        <h3>
          <span v-if="countPartners === 1">Partner projektu</span>
          <span v-else>Partnerzy projektu</span>
        </h3>
      </div>
      <div
        class="modal__list"
        v-for="(partner, index) in selectedProject.partner"
        :key="index"
      >
        <span class="modal__list-name">{{ partner.name }}</span>
        <a
          class="modal__list-anchor btn-primary"
          :href="partner.link"
          target="blank"
        >
          <span>Poznaj</span>
          <i class="btn-icon fas fa-hands-helping"></i>
        </a>
      </div>
    </div>
    <div v-show="countTech > 0">
      <div class="modal__title">
        <h3>Wykorzystane technologie</h3>
      </div>
      <div class="modal__list">
        <a
          class="btn-primary"
          v-for="(item, index) in selectedProject.stack"
          :key="index"
          :href="item.documentation"
          target="_blank"
        >
          {{ item.name }}
        </a>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  props: ['selectedProject'],
  methods: {
    onClick() {
      this.$root.$emit('close');
    }
  },
  computed: {
    countPartners() {
      return this.selectedProject.partner.length;
    },
    countTech() {
      return this.selectedProject.stack.length;
    }
  }
};
</script>

<style lang="scss" scoped>
@import './../main.scss';

h2 {
  font-size: 2.5rem;
  color: $white;
  text-align: center;
  max-width: 75%;
}

.modal {
  background: $white;
}

.modal__button-close {
  position: absolute;
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1;
  right: 3%;
  height: 3.2rem;
  width: 3.2rem;
  font-size: 2.5rem;
  color: $white;
  border-radius: 45px;
  border: $white solid 3px;
}

.modal__button-close:active,
.modal__button-close:hover {
  color: $blue;
  background-color: $white;
  cursor: pointer;
}

.modal__description,
.modal__list,
.modal__title {
  padding: 0.5rem 1.5rem;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
}

.modal__list {
  flex-wrap: wrap;
  width: 35rem;
  margin: auto;
}

.modal__list-name {
  text-align: center;
  width: 15rem;
}

.modal__list-anchor {
  margin-left: 1rem;
  display: flex;
  align-items: center;
}

.modal > .modal__title {
  background: $blue;
}

@media only screen and (max-width: $phone) {
  h2,
  h3 {
    text-align: center;
  }
  h2 {
    font-size: 1.4rem;
    width: 80%;
    margin: 0;
  }
  .modal__button-close {
    position: fixed;
    top: 90%;
    background-color: $blue;
    border: $blue solid 3px;
  }
  .modal__list {
    width: 15rem;
  }
  .modal__title {
    display: flex;
    justify-content: center;
  }
}
</style>
