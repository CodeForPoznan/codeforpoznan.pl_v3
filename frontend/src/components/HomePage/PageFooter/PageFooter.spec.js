import { shallowMount } from '@vue/test-utils';
import PageFooter from './PageFooter';

describe('PageFooter component', () => {
  it('renders correctly', () => {
    const wrapper = shallowMount(PageFooter);

    expect(wrapper).toBeDefined();
  });
});
