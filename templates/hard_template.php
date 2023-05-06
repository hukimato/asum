<#for data as method#>

class <#path#><#method.key#>Model extends BaseModel
{
    <#for method.value.responses.200.content.application/json.schema.properties as property#>
        <#if property.value.type == 'array'#>
            public <#property.key#> = [];
        <#else#>
            public <#property.value.type#> <#property.key#>;
        <#endif#>
    <#endfor#>
}

<#endfor#>

