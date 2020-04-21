import React from "react"
import { connectToStreamlit, StreamlitComponent } from "./streamlit"

import Highcharts from "highcharts"
import Exporting from "highcharts/modules/exporting"

import "bootstrap/dist/css/bootstrap.min.css"

Exporting(Highcharts)


interface State {
  numClicks: number
}

class MyComponent extends StreamlitComponent<State> {
  public state = { numClicks: 0 }

  public updateChart(): void{
    let options = this.props.args["options"] || {}
    Highcharts.chart('container', options)

    this.props.updateFrameHeight()
  }

  public componentDidMount(): void {
    this.updateChart()
  }

  public componentDidUpdate(): void {
    this.updateChart()
  }

  public render = (): React.ReactNode => {
    let name = this.props.args["name"] || "unspecified"

    return (
      <figure className="highcharts-figure">
        <label>{name}</label>
        <div id="container"/>
      </figure>
    )
  }

  /*
  private onClicked = (): void => {
    this.setState(
      prevState => ({ numClicks: prevState.numClicks + 1 }),
      () => this.props.setWidgetValue(this.state.numClicks)
    )
  }
  */
}

export default connectToStreamlit(MyComponent)
