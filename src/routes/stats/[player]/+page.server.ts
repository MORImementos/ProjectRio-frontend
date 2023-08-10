import { STAT_ENDPOINTS, GET } from '$lib/constants';

export const load = async ({ params }) => {
    const { player } = params; // Get the value of the "player" parameter from the route
    
    const data = await GET(STAT_ENDPOINTS.STATS + `?tag=starsoffseason6&username=${player}`);
    // console.log(data);
    
    return { data };
};
