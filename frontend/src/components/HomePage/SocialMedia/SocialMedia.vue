<template>
  <div id="media">
    <h2>MEDIA</h2>
    <ul class="media-info">
      <li v-for="item in media" :key="item.link">
        <a :href="item.link" target="_blank" class="circle">
          <v-icon> {{ item.icon }} </v-icon>
        </a>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      media: [
        {
          icon: 'fab fa-github',
          link: 'https://github.com/CodeForPoznan'
        },
        {
          icon: 'fab fa-linkedin-in',
          link: 'https://www.linkedin.com/company/codeforpoznan/'
        },
        {
          icon: 'fab fa-facebook-f',
          link: 'https://www.facebook.com/CodeForPL/'
        },
        {
          icon: 'fab fa-slack',
          link:
            'https://join.slack.com/t/codeforpoznan/shared_invite/zt-8a7u52j8-yqB01C2YgYF4Lvd1pFM_jw'
        }
      ]
    };
  }
};
</script>

<style lang="scss" scoped>
@import '../../../main.scss';
#media {
  color: $white;
  background-color: $blue-media-hr;
  text-align: center;
}
h2 {
  font-size: 24px;
  padding: 60px 0 20px 0;
  color: $white;
}
.circle {
  border: 2px solid $white;
  width: 50px;
  height: 50px;
  border-radius: 50%;
}
ul.media-info {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 20px 0 60px 0;
}
li {
  list-style-type: none;
  margin: 0 10px;
}
a {
  display: inline-block;
}
a:hover {
  background-size: 100% 100%;
  background-color: $white;
  .v-icon {
    color: $blue-media-hr;
  }
}
.v-icon {
  color: $white;
  padding: 10px;
  border-radius: 50%;
}
</style>
