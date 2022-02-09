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
        <i class="btn-icon far fa-copyright"></i>
        <span class="btn-text">Licencja</span>
      </a>
      <a
        v-show="selectedProject.githubLink !== ''"
        class="btn-transparent"
        :href="selectedProject.githubLink"
        target="blank"
      >
        <i class="btn-icon fab fa-github"></i>
        <span class="btn-text">Repozytorium</span>
      </a>
      <a
        v-show="selectedProject.website !== ''"
        class="btn-transparent"
        :href="selectedProject.website"
        target="blank"
      >
        <i class="btn-icon fas fa-globe"></i>
        <span class="btn-text">Strona projektu</span>
      </a>
    </div>
    <div class="modal__description">
      <p>{{ selectedProject.description }}</p>
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
          class="btn-primary modal__list-anchor"
          :href="partner.link"
          target="blank"
        >
          <span class="btn-text">Poznaj</span>
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
          <i class="btn-icon" :class="item.icon"></i>
          <span class="btn-text">{{ item.name }}</span>
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
@import '../../../../main.scss';

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
  text-align: center;
}

.modal__list {
  flex-wrap: wrap;
  width: 70%;
  margin: auto;
}

.modal__list-name {
  text-align: center;
  width: 45%;
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
    width: 90%;
  }
  .modal__list-name {
    width: 70%;
  }
  .modal__title {
    display: flex;
    justify-content: center;
  }
}
</style>
