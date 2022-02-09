import { shallowMount } from '@vue/test-utils';
import ModalContent from './ModalContent';

describe('ModalContent component', () => {
  it('renders correctly', () => {
    const wrapper = shallowMount(ModalContent, {
      propsData: { selectedProject: { partner: [], stack: [] } }
    });

    expect(wrapper).toBeDefined();
  });
});
