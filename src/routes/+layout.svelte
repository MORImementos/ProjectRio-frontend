<script lang='ts'>
	// The ordering of these imports is critical to your app working properly
	// import '@skeletonlabs/skeleton/themes/theme-modern.css';
	import '../theme.postcss'
	// If you have source.organizeImports set to true in VSCode, then it will auto change this ordering
	import '@skeletonlabs/skeleton/styles/skeleton.css';
	// Most of your app wide CSS should be put in this file
	import '../app.postcss';

	import { AppShell } from '@skeletonlabs/skeleton';
</script>
<div class="h-full overflow-hidden contents">
<AppShell class="w-full h-full flex flex-col overflow-hidden">

	
	<slot />

</AppShell>
</div>
