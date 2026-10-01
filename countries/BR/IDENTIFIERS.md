# Brazil Jurisdiction Identifier Model

OSINT4ALL supports jurisdiction-specific identifiers as `BR:<identifier>`, derived from the structured input model reviewed in OSINT Brazuca.

Examples include `BR:cpf`, `BR:cnpj`, `BR:case-number`, `BR:oab`, `BR:vehicle-plate`, `BR:renavam`, `BR:cep`, `BR:property-registration`, `BR:rural-environmental-registry`, `BR:aircraft-registration`, `BR:cnes` and `BR:ibge-code`.

The complete controlled list lives in `data/taxonomies.json`.

## Privacy rule

An identifier existing in the taxonomy does not authorize indiscriminate collection. For personal data, document purpose, source, necessity and applicable legal basis; minimize retained data. A regex match proves only a pattern match, not identity or document validity.

## Planned normalization

The OSINT Brazuca structured dataset can map into OSINT4ALL as:

`input → jurisdiction_inputs`  
`output → output_types`  
`tipo_fonte → authority_scope`  
`links[].uf → BR subdivision`

Every imported child source should initially be **needs-review**.
