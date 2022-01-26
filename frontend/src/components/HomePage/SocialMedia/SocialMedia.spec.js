import { shallowMount } from '@vue/test-utils';
import { getMountWithVuetify } from '../../../../jest/utils';
import SocialMedia from './SocialMedia';

describe('SocialMedia component', () => {
  const mountWithVuetify = getMountWithVuetify();

  it('renders the title', () => {
    const wrapper = shallowMount(SocialMedia);

    expect(wrapper.get('h2').text()).toBe('MEDIA');
  });
  it('renders a list of social media items', () => {
    const wrapper = shallowMount(SocialMedia);

    expect(wrapper.get('.media-info').isVisible()).toBe(true);
  });
  it('renders a list item for each social medium', () => {
    const wrapper = shallowMount(SocialMedia);

    expect(wrapper.findAll('li')).toHaveLength(4);
  });
  it('renders correct icon for github', () => {
    const wrapper = mountWithVuetify(SocialMedia);

    expect(wrapper.get('.fab.fa-github').isVisible()).toBe(true);
  });
  it('renders correct link for github', () => {
    const wrapper = mountWithVuetify(SocialMedia);

    expect(
      wrapper.get('[href="https://github.com/CodeForPoznan"]').isVisible()
    ).toBe(true);
  });
  it('renders correct icon for linkedIn', () => {
    const wrapper = mountWithVuetify(SocialMedia);

    expect(wrapper.get('.fab.fa-linkedin-in').isVisible()).toBe(true);
  });
  it('renders correct link for linkedIn', () => {
    const wrapper = mountWithVuetify(SocialMedia);

    expect(
      wrapper
        .get('[href="https://www.linkedin.com/company/codeforpoznan/"]')
        .isVisible()
    ).toBe(true);
  });
  it('renders correct icon for facebook', () => {
    const wrapper = mountWithVuetify(SocialMedia);

    expect(wrapper.get('.fab.fa-facebook-f').isVisible()).toBe(true);
  });
  it('renders correct link for facebook', () => {
    const wrapper = mountWithVuetify(SocialMedia);

    expect(
      wrapper.get('[href="https://www.facebook.com/CodeForPL/"]').isVisible()
    ).toBe(true);
  });
  it('renders correct icon for slack', () => {
    const wrapper = mountWithVuetify(SocialMedia);

    expect(wrapper.get('.fab.fa-slack').isVisible()).toBe(true);
  });
  it('renders correct link for slack', () => {
    const wrapper = mountWithVuetify(SocialMedia);

    expect(
      wrapper
        .get(
          '[href="https://join.slack.com/t/codeforpoznan/shared_invite/zt-8a7u52j8-yqB01C2YgYF4Lvd1pFM_jw"]'
        )
        .isVisible()
    ).toBe(true);
  });
});
