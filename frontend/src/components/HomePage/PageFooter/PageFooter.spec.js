import { shallowMount } from '@vue/test-utils';
import PageFooter from './PageFooter.vue';
import { expect, test, it } from 'vitest';

test('PageFooter component', () => {
  it('renders correctly', () => {
    const wrapper = shallowMount(PageFooter);

    expect(wrapper).toBeDefined();
  });
});
