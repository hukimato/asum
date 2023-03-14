class <#path#>Model extends BaseModel
{
    <#for data.put.responses.200.content.application/json.schema.properties as property#>
    public <#property.value.type#> <#property.key#>;
    <#endfor#>


}
