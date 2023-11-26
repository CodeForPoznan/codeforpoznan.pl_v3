import { getMountWithProviders } from '../../../../jest/utils';
import HacknightsParticipants from './HacknightsParticipants.vue';
import { expect, test, it } from 'vitest';

test('HacknightsParticipants component', () => {
  const mountWithProviders = getMountWithProviders();

  it('renders correctly', () => {
    const wrapper = mountWithProviders(HacknightsParticipants);

    expect(wrapper).toBeDefined();
  });
});
