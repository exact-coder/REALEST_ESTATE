import React from 'react';
import Card from './Card';

const Listings = ( {listings} ) => {
  const getListings = () => {
    let listingOnPage = [];
    let result =[];

    listings.map(listing =>  {
      return listingOnPage.push(
        <Card
          title={listing.title}
          address={listing.address}
          city={listing.city}
          state={listing.state}
          price={listing.price}
          sale_type={listing.sale_type}
          home_type={listing.home_type}
          bedrooms={listing.bedrooms}
          bathrooms={listing.bathrooms}
          sqft={listing.sqft}
          photo_main={listing.photo_main}
          slug={listing.slug}
        />
      )
    })

    for(let i =0; i<listings.length; i+= 3) {
      result.push(
        <div className='row'>
          <div className="col-1-of-3">
            {listingOnPage[1]}
          </div>
          <div className="col-1-of-3">
            {listingOnPage[i+1] ? listingOnPage[i+1] : null}
          </div>
          <div className="col-1-of-3">
          {listingOnPage[i+2] ? listingOnPage[i+2] : null}
          </div>
          <div className="col-1-of-3">
            {listingOnPage[1]}
          </div>
        </div>
      )
    };
    return result;
  }
  
  return (
    <div>
      {getListings()}
      {console.log(getListings())}
    </div>
    
  )
}

export default Listings;
