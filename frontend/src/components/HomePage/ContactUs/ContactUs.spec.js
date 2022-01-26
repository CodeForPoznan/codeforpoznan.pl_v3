import { shallowMount } from '@vue/test-utils';
import ContactUs from './ContactUs';

describe('ContactUs component', () => {
  it('renders correctly', () => {
    const wrapper = shallowMount(ContactUs);

    expect(wrapper).toBeDefined();
  });
});
