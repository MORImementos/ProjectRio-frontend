import { STAT_ENDPOINTS, GET } from '$lib/constants';
// import type { PageServerLoad } from './$types'

// fetch stats on page load
export const load = async ({ fetch }) => {
    const data = await GET(STAT_ENDPOINTS.STATS + "?tag=starsoffseason5&username=mori&limit_games=10")
    console.log(data);
    return {data: data}

}