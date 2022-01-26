import Hacknight from './Hacknight';
import { getMountWithProviders } from '../../../../jest/utils';

describe('Hacknight component', () => {
  const mountWithProviders = getMountWithProviders();

  it('renders correctly', () => {
    const wrapper = mountWithProviders(Hacknight);

    expect(wrapper).toBeDefined();
  });
});
