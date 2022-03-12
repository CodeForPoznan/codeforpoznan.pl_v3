import { getMountWithProviders } from '../../../jest/utils';
import HomePage from './HomePage';

describe('HomePage component', () => {
  const mountWithProviders = getMountWithProviders();

  it('renders correctly', () => {
    const wrapper = mountWithProviders(HomePage);

    expect(wrapper).toBeDefined();
  });
});
