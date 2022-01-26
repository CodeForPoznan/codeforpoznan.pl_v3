import Dashboard from './Dashboard';
import { getMountWithProviders } from '../../../jest/utils';

describe('Dashboard component', () => {
  const mountWithProviders = getMountWithProviders();

  it('renders correctly', () => {
    const wrapper = mountWithProviders(Dashboard);

    expect(wrapper).toBeDefined();
  });
});
