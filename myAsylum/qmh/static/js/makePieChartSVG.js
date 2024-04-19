//code adapted from d3.org
function makePieChartSVG(obj) {
        d3.csv(obj.csv, function(err, rows) {
            function unpack(rows, key) {
                return rows.map(function(row) {return row[key];});
            }

            let labels = unpack(rows, obj.labels),
                values = unpack(rows, obj.values)

            let data = {};
            for (let i = 0; i < labels.length; i++) {
                (data[labels[i]] = values[i]);
            }

            let width = 250,
                height = 250,
                margin = 20

            let radius = Math.min(width, height) / 2 - margin
                
            let svg = d3.select(obj.div)
                .append("svg")
                .attr("width", width)
                .attr("height", height)
                .append("g")
                .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")");

            let pie = d3.pie()
                .value(function(d) {return d.value; })

            let data_ready = pie(d3.entries(data))

            let arcGenerator = d3.arc()
                .innerRadius(0)
                .outerRadius(radius)

            svg
                .selectAll('mySlices')
                .data(data_ready)
                .enter()
                .append('path')
                .attr('d', arcGenerator)
                .attr('fill', function(d){ return(obj.color[d.data.key]) })
                .attr("stroke", "black")
                .style("stroke-width", "2px")
                .style("opacity", 0.7)

            svg
                .selectAll('mySlices')
                .data(data_ready)
                .enter()
                .append('text')
                .text(function(d){ return d.data.key + ", " + d.data.value})
                .attr("transform", function(d) { return "translate(" + arcGenerator.centroid(d) + ")";  })
                .style("text-anchor", "middle")
                .style("font-size", 17)
            
        })

}