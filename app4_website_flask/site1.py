from flask import Flask, render_template

app=Flask(__name__)

@app.route('/plot/')
def plot():
    from pandas_datareader import data
    import datetime
    from bokeh.plotting import figure
    from bokeh.io import output_file, show
    from bokeh.embed import components
    from bokeh.resources import CDN

    start=datetime.datetime(2018,3,1)
    end=datetime.datetime(2018,11,1)
    df=data.DataReader(name="LMT", data_source="yahoo",start=start,end=end)

    def inc_dec(c,o):
        if o>c:
            return "Increase"
        elif c>o:
            return "Decrease"
        else:
            return "equal"

    df["Status"]=[inc_dec(c,o) for c,o in zip(df.Close,df.Open)]
    df["Middle"]=(df.Open+df.Close)/2
    df["Height"]=abs(df.Open-df.Close)

    # set up the bokeh figure

    r=figure(plot_width=1000,plot_height=400, x_axis_type="datetime")
    # r.title.text="Candlestick Chart"
    # r.title.text_color="Gray"
    # r.title.text_font="times"
    # r.title.text_font_style="bold"
    # r.title.text_font_size="20pt"
    # r.title.align="center"
    r.grid.grid_line_alpha=0.3

    # 12 hours in milliseconds
    hr=12*60*60*1000

    # display rectangles for candlestick display
    z=r.segment(df.index,
                df.High,
                df.index,
                df.Low,
                color="black")
    z=r.rect(x=df.index[df.Status=="Increase"],
             y=df.Middle[df.Status=="Increase"],
             width=hr,
             height=df.Height[df.Status=="Increase"],
             fill_color="#CCFFFF",
             line_color="black")
    z=r.rect(x=df.index[df.Status=="Decrease"],
             y=df.Middle[df.Status=="Decrease"],
             width=hr,
             height=df.Height[df.Status=="Decrease"],
             fill_color="#FF3333",
             line_color="black")

    script1, div1 = components(r)
    cdn_js=CDN.js_files[0]
    cdn_css=CDN.css_files[0]
    return render_template("plot.html",
                            script1=script1,
                            div1=div1,
                            cdn_js=cdn_js,
                            cdn_css=cdn_css)

@app.route('/')
def home ():
    return render_template("home.html")

@app.route('/about/')
def about ():
    return render_template("about.html")

if __name__=="__main__" :
    app.run(debug=True)
