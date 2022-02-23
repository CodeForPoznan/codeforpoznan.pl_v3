import { getMountWithProviders } from '../../../../jest/utils';
import HacknightsParticipants from './HacknightsParticipants';

describe('HacknightsParticipants component', () => {
  const mountWithProviders = getMountWithProviders();

  it('renders correctly', () => {
    const wrapper = mountWithProviders(HacknightsParticipants);

    expect(wrapper).toBeDefined();
  });
});
