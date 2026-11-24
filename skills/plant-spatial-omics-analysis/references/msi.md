# MSI branch: existing plant imaging data

Use this branch to interpret or compare saved mass spectrometry imaging (MSI) features, not to infer experimental parameters from a screenshot or replace an established workflow.

1. **Bind the source values and image.** Record feature identifiers and whether a value is a raw response, normalized response, or display transformation. Bind each image to sample, section, ROI, coordinate axes, orientation, and source table. Check registration before claiming that regions correspond.
2. **Separate analytical and display choices.** Track normalization, smoothing, interpolation, clipping and color-scale choices independently. A visual contrast change does not establish a biological change. Separately scaled panels should not be compared as though their colors measure the same intensity. A shared scale alone does not make signal an absolute concentration.
3. **Keep chemical claims at the observed evidence level.** An ion feature is not a confirmed compound. If reporting a candidate match, document the relevant evidence type and the uncertainty; distinguish annotation from spatial pattern. Do not pool multiple features as unique molecules without evidence that justifies the grouping.
4. **Define denominators and units.** State explicitly whether a fraction or mean uses all valid pixels, a defined ROI, or only assigned pixels. A difference in denominators can change the result; one good-looking overlay is not validation. Repeated pixels or adjacent sections are not independent biological replicates.
5. **Report the physical comparison accurately.** Separate observed within-section position, inferred tissue annotation, and cross-section alignment. Similar patterns or co-distribution do not establish causal or mechanistic relationships.

If one condition has differently scaled saved images, state what remains interpretable qualitatively. Re-render from compatible, approved source values only when authorized and needed. Do not improvise numerical intensity from colors.

## When annotation sources or comparison groups change

Count coverage by distinct observed features in the eligible set, not by candidate rows. Report proposed formula or entity ambiguity and class agreement separately. Multiple reference sources may suggest different candidates for one feature; retain disagreement. For cross-group alignment, distinguish reliable feature alignment, a target-list candidate match, no reliable match in retained features, and a measured zero. An unmatched or excluded feature is not evidence of biological absence. Never join independently numbered clusters by label alone.

Check coordinates against table rows and masks, along with orientation, registration, comparable coverage and the denominator. If alignment or scaling choices could change the interpretation, compare defensible alternatives when authorized; report separately whether saved quantitative differences are stable across analytical choices and whether visual contrasts change across display scales. A display-only reversal does not change a stored measurement. Pair a co-distribution observation with plausible physical or technical explanations before suggesting biology.
